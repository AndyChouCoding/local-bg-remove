#!/bin/bash
cd "$(dirname "$0")"

echo "=== 去背工具 ==="
echo ""

if ! command -v python3 &> /dev/null; then
    echo "錯誤：找不到 python3，請先安裝 Python 3。"
    exit 1
fi

if ! python3 -c "import rembg" &> /dev/null; then
    echo "首次執行，安裝依賴套件..."
    pip3 install -r requirements.txt
    echo ""
fi

python3 remove_bg.py

echo ""
read -p "按 Enter 關閉視窗..."
osascript -e 'tell application "Terminal" to close front window'
