import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import mermaid

class MermaidPreprocessor(Preprocessor):
    def run(self, lines):
        for i, line in enumerate(lines):
            if line.strip().startswith("~~~mermaid"):
                code_block = []
                for subline in lines[i+1:]:
                    if subline.strip().startswith("~~~"):
                        break
                    code_block.append(subline)
                mermaid_code = "".join(code_block)
                svg_code = mermaid.mermaid2svg(mermaid_code)
                lines[i] = f'<div class="mermaid">{svg_code}</div>'
        return lines

class MermaidExtension(Extension):
    def extendMarkdown(self, md):
        mermaid_preprocessor = MermaidPreprocessor(md)
        md.preprocessors.register(mermaid_preprocessor, "mermaid", 175)

text = """
# Title

Some text.

~~~mermaid
graph TB
A --> B
B --> C
~~~

Some other text.

~~~mermaid
graph TB
D --> E
E --> F
~~~
"""

html = markdown.markdown(text, extensions=[MermaidExtension()])

print(html)