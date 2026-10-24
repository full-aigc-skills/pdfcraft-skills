"""开发场景与已发行基础技能分开注册，不跳过内容摘要校验。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('print_package_candidates',ROOT/'scripts/validate_package.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class CandidateTests(unittest.TestCase):
    def test_candidate_is_allowed_but_tampered_content_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);folder=root/'skills/pdfcraft-example';folder.mkdir(parents=True)
            (root/'skill-suite.json').write_text(json.dumps({'domain':'printcraft','skills':[]}))
            body='---\nname: pdfcraft-example\ndescription: example\n---\n';(folder/'SKILL.md').write_text(body)
            (root/'scenario-candidates.json').write_text(json.dumps({'status':'local-unreleased','sourcePackage':'full-aigc-skills/pdfcraft-skills','skills':[{'name':'pdfcraft-example','sha256':hashlib.sha256(body.encode()).hexdigest()}]}))
            original=m.ROOT
            try:
                m.ROOT=root;self.assertEqual(m.validate()['structure'],'PASS')
                (folder/'SKILL.md').write_text(body+'changed\n')
                with self.assertRaisesRegex(ValueError,'candidate_digest_mismatch'):m.validate()
            finally:m.ROOT=original
