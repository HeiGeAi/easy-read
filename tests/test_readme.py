"""Keep the showcased thyroid example qualified and source-backed."""

from pathlib import Path
import unittest


class TestReadmeMedicalExample(unittest.TestCase):
    def test_tsh_example_and_source(self):
        readme = (Path(__file__).resolve().parents[1] / "README.md").read_text(encoding="utf-8")
        before = "TSH 偏高，建议结合 FT4 等检查评估甲状腺功能"
        self.assertEqual(readme.count(before), 2)
        example = next(line for line in readme.splitlines() if "翻译后" in line and "TSH" in line)
        for qualifier in ("通常", "可能不够活跃", "不能只凭这一项下诊断", "FT4", "症状"):
            self.assertIn(qualifier, example)
        self.assertNotIn("甲状腺太亢奋", readme)
        self.assertNotIn("TSH 偏高，建议排查甲状腺功能亢进", readme)
        self.assertIn("https://www.niddk.nih.gov/health-information/diagnostic-tests/thyroid", readme)
        self.assertIn("不能代替医生诊断", readme)


if __name__ == "__main__":
    unittest.main()
