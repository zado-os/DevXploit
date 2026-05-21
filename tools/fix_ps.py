import re
p = "modules/exploits/prestashop_exploits.py"
t = open(p, encoding="utf-8").read()
old = r"        statusCheck = re\.findall\(r'DevXploit', getattr\(checkShell, 'text', ''\) or ''\)\n        if statusCheck:\n            return dict\(\n                url=self\.url,\n                name=\"([^\"]+)\",\n                status=True,\n                shell=([^\n]+)\n            \)\n        else:\n            return dict\(\n                url=self\.url,\n                name=\"\1\",\n                status=False\n            \)"
new = r"        ok = self._shell_ok(\2)\n        return dict(url=self.url, name=\"\1\", status=ok, shell=\2 if ok else None)"
t2, n = re.subn(old, new, t)
open(p, "w", encoding="utf-8").write(t2)
print("fixed", n)
