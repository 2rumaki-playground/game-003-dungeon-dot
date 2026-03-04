# 現在の作業をcommit・push・PR作成

## 指示

現在のブランチの変更をコミットし、リモートにpushし、PRを作成してください。

### 1. 状態確認

以下を並列実行して現在の状態を把握する:

- `git status` で未コミットの変更を確認
- `git diff` でステージされていない変更の内容を確認
- `git log --oneline main..HEAD` でmainからの全コミット履歴を確認
- `git diff main...HEAD --stat` でmainからの変更ファイル一覧を確認
- `git ls-remote --heads origin "$(git rev-parse --abbrev-ref HEAD)"` で現在のブランチがリモートに存在するか確認

### 2. 依存関係のインストール

```
task install
```

### 3. コミット前チェック

以下を順に実行し、問題があれば修正する:

1. `task format` — フォーマット適用
2. `task lint` — リントチェック
3. `task typecheck` — 型チェック
4. `task deps:check` — 依存方向チェック
5. `task test` — ユニットテスト全通過を確認

問題が見つかった場合は修正してから次に進む。

### 4. 仕様書同期の確認

コミット対象の変更が `docs/spec/` 配下の仕様ドキュメントに影響するかを確認する:

1. 以下3つのコマンドで取得した変更ファイル一覧の和集合を取る:
   - `git diff main...HEAD --name-only`（main から分岐後にコミット済みの変更）
   - `git diff --name-only`（未ステージの作業ツリー変更）
   - `git diff --cached --name-only`（ステージ済みの変更）
2. 変更ファイルに以下が含まれる場合、対応する仕様ドキュメントの更新が必要か確認する:
   - `constants.py` → `docs/spec/constants.md` の更新が必要か確認
   - `domain/`, `presentation/`, `infrastructure/` 配下のファイル → 関連する `docs/spec/` のドキュメントに影響がないか確認
3. 仕様ドキュメントの更新が必要な場合は、対応するドキュメントも更新してからコミットに含める
4. 新しい仕様ドキュメントを追加した場合は `docs/spec/readme.md` の一覧も更新する

### 5. コミット

- 未コミットの変更がある場合のみコミットする（変更がなければスキップ）
- Conventional Commits形式、日本語、50文字以内
- `.github/git-commit-instructions.md` に記載のtype一覧（feat/fix/docs/refactor/test/chore/perf/style）から選択
- 関連ファイルを個別に `git add` する（`git add .` は使わない）

### 6. Push

- `git push -u origin <ブランチ名>` でリモートにpush

### 7. PR作成

- 既にこのブランチのPRが存在するか `gh pr list --head <ブランチ名>` で確認
- PRが既に存在する場合はpushのみで完了（PRのURLを表示する）
- PRが存在しない場合は以下の形式で新規作成:

```
gh pr create --base main --title "<type>: <日本語の説明>" --body "$(cat <<'EOF'
## 概要
<mainからの全変更内容を分析した箇条書き>

Closes #<関連Issue番号（ブランチ名から推測）>

## テスト計画
<テスト方法のチェックリスト>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

- PRタイトルはConventional Commits形式、日本語、70文字以内
- PRの概要にはmainからの**全コミット**の変更内容を反映する（最新コミットだけでなく）
- ブランチ名に含まれるIssue番号から `Closes #<番号>` を生成する
- 最後にPRのURLを表示する
