# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]
### Added
### Fixed
### Changed

---

## [v1.0.2] - 2026-04-16
### Fixed
- Terminal window now closes automatically after pressing Enter (`osascript`)

### Fixed（修復）
- 按 Enter 後 Terminal 視窗自動關閉

---

## [v1.0.1] - 2026-04-16
### Changed
- Renamed `run.sh` to `run.command` for double-click execution on macOS
- Added "Press Enter to close" prompt at the end of execution

### Changed（變更）
- `run.sh` 更名為 `run.command`，支援 Finder 雙擊執行
- 執行結束後顯示「按 Enter 關閉視窗」提示

---

## [v1.0.0] - 2026-04-16
### Added
- Local background removal tool using rembg (U2Net model)
- Batch processing of all images in `source/` folder
- Supports .png / .jpg / .jpeg / .webp input formats
- Output saved as .png (transparent background) with original filename to `output/`
- `run.command` one-click execution script with auto dependency install
- Bilingual README (English / 中文)

### Added（新增）
- 本地去背工具，使用 rembg（U2Net 模型）
- 批次處理 `source/` 資料夾內所有圖片
- 支援 .png / .jpg / .jpeg / .webp 輸入格式
- 輸出保留原檔名，統一存為 .png（透明背景）至 `output/` 資料夾
- `run.command` 一鍵執行腳本，自動安裝依賴套件
- 雙語 README（英文 / 中文）
