import sys

"""
reverse inputpath outputpath: inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
copy inputpath outputpath: inputpath にあるファイルのコピーを作成し、outputpath として保存します。
duplicate-contents inputpath n: inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
replace-string inputpath needle newstring: inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
"""
# コマンドライン引数からコマンドを取得
command = sys.argv[1]

# reverse コマンド: 入力ファイルの内容を反転させて出力ファイルに書き出す
if command == "reverse":
    with open(sys.argv[2]) as f:
        contents = f.read()[::-1]
    with open(sys.argv[3],'w') as f:
        f.write(contents)

# copy コマンド: 入力ファイルのコピーを作成して出力ファイルに保存する
elif command == "copy":
    with open(sys.argv[2]) as f:
        contents = f.read()
    with open(sys.argv[3],'w') as f:
        f.write(contents)

# duplicate-contents コマンド: 入力ファイルの内容を複製し、指定回数だけ入力ファイルに追加する
elif command == "duplicate-contents":
    with open(sys.argv[2]) as f:
        contents = f.read()
    for i in range(int(sys.argv[3])):
        with open(sys.argv[2],'a') as f:
            f.write(contents)

# replace-string コマンド: 入力ファイルの内容から指定の文字列を検索し、別の文字列に置き換える
elif command == "replace-string":
    with open(sys.argv[2]) as f:
        contents = f.read().replace(sys.argv[3],sys.argv[4])
    with open(sys.argv[2],'w') as f:
        f.write(contents)

# コマンドが見つからない場合はエラーメッセージを表示する
else:
    print("error: command not found")