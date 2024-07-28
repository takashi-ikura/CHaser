import CHaser # 同じディレクトリに CHaser.py がある前提

def main():
    value = [] # フィールド情報を保存するリスト
    client = CHaser.Client() # サーバーと通信するためのインスタンス

    while(True):
        value = client.get_ready() # サーバーに行動準備が完了したと伝える
        #input("key:")
        if value[7] != 2:
            value = client.walk_down()
        else:
            value = client.put_up()

if __name__ == "__main__":
    main()