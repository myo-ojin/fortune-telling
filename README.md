# 複数占い手法統合システム (Multi-Method Fortune Telling System)

データベース駆動型のアーキテクチャで、5つ以上の占い手法を統合し、多角的な運勢分析を提供する占いアプリケーション。

## セットアップ

### 必要な環境
- Python 3.11以上

### インストール手順

1. **リポジトリのクローン**
```bash
git clone <repository-url>
cd fortune-telling
```

2. **仮想環境の作成**
```bash
python -m venv venv
```

3. **仮想環境のアクティベート**

Linux/Mac:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

4. **依存パッケージのインストール**
```bash
pip install -r requirements.txt
```

5. **動作確認**
```bash
python -c "import flask; import swisseph; print('Setup OK')"
```

## 実装状況

### Phase 1a: MVP Core（進行中）
- [x] T001: プロジェクト構造の作成
- [x] T002: Python仮想環境のセットアップ
- [x] T003: Flaskアプリケーションの基本構成
- [ ] T004-T019: 継続中...

## プロジェクト構造

```
fortune-telling/
├── app/                  # アプリケーション本体
│   ├── fortune/         # 占い手法モジュール
│   ├── templates/       # HTMLテンプレート
│   └── static/          # CSS, JavaScript
├── data/                # データベースとシードデータ
├── tests/               # テストコード
├── config.py            # 設定ファイル
├── run.py               # アプリケーション起動
└── requirements.txt     # Pythonパッケージ
```

## 使用技術

- **バックエンド**: Flask 3.0.0
- **データベース**: SQLite + SQLAlchemy 2.0.23
- **占い計算**: pyswisseph 2.10.3.2
- **テスト**: pytest 7.4.3

## ドキュメント

- [要件定義書](.kiro/specs/multi-method-fortune-telling/requirements.md)
- [設計書](.kiro/specs/multi-method-fortune-telling/design.md)
- [実装タスクリスト](.kiro/specs/multi-method-fortune-telling/implementation-tasks.md)

## ライセンス

TBD
