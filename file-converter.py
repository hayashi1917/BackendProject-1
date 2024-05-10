import markdown
import sys


def convert_markdown_to_html(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    html = markdown.markdown(contents)
    with open(outputpath,'w') as f:
        f.write(html)
        
# コマンドライン引数からコマンドを取得
command = sys.argv[1]

# convert-markdown-to-html コマンド: 入力ファイルの Markdown を HTML に変換して出力ファイルに書き出す
if command == "markdown":
    convert_markdown_to_html(sys.argv[2], sys.argv[3])
else:
    print("error: command not found")