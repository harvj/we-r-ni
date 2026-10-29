import hashlib
from pathlib import Path
import tempfile
import subprocess
import sys
import unittest
from scripts.squarespace_inventory import inventory, summary

FIXTURES = Path(__file__).parent / 'fixtures'


class InventoryTests(unittest.TestCase):
    def test_extraction_unicode_missing_fields_and_repeatability(self):
        path = FIXTURES / 'pages.xml'
        before = hashlib.sha256(path.read_bytes()).digest()
        data = inventory(FIXTURES)
        self.assertEqual(data, inventory(FIXTURES))
        self.assertEqual(before, hashlib.sha256(path.read_bytes()).digest())
        self.assertEqual(data['item_count'], 2)
        page = data['pages'][0]
        self.assertEqual(page['title'], 'י Α संस्कृत ☉ ䷀')
        self.assertEqual(page['original_path'], '/智慧')
        self.assertEqual(page['publication_date'], 'Fri, 19 Jun 2026 02:21:22 +0000')
        self.assertIn('Hello world & friends.', page['readable_text'])
        self.assertNotIn('secret', page['readable_text'])
        self.assertNotIn('hidden', page['readable_text'])
        self.assertIn('secret()', page['source_html'])
        self.assertEqual(page['outgoing_links'], ['/next'])
        self.assertEqual(page['image_urls'], ['/a.jpg', '/b.jpg', '/c.jpg', '/d.jpg'])
        self.assertIsNone(data['pages'][1]['title'])
        self.assertEqual(len(data['problems']), 4)
        self.assertIn('י Α संस्कृत ☉ ䷀', summary(data))

    def test_bad_xml_does_not_prevent_other_exports(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'bad.xml').write_text('<rss>', encoding='utf-8')
            (root / 'good.xml').write_bytes((FIXTURES / 'pages.xml').read_bytes())
            data = inventory(root)
            self.assertEqual(data['item_count'], 2)
            self.assertTrue(any(p['source'] == 'bad.xml' for p in data['problems']))

    def test_cli_outputs_count_validation_and_source_guard(self):
        script = Path(__file__).resolve().parents[1] / 'scripts/squarespace_inventory.py'
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            command = [sys.executable, str(script), '--source-dir', str(FIXTURES),
                       '--output-dir', str(root / 'output'), '--summary', str(root / 'summary.md'),
                       '--expect-count', '3']
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn('Expected 3 items.', result.stderr)
            self.assertTrue((root / 'output/squarespace.json').exists())
            self.assertTrue((root / 'summary.md').exists())
            result = subprocess.run(command + ['--summary', str(FIXTURES / 'forbidden.md')],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertFalse((FIXTURES / 'forbidden.md').exists())

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            data = inventory(Path(directory))
            self.assertEqual(data['item_count'], 0)
            self.assertEqual(len(data['problems']), 1)


if __name__ == '__main__':
    unittest.main()
