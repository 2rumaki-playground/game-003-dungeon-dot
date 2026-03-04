#!/bin/bash
# git commit 前に ruff format + lint を実行するフック

set -e

input_json=$(cat)
command=$(echo "$input_json" | jq -r '.tool_input.command // empty')

# git commit コマンド以外はスキップ
if [[ "$command" != *"git commit"* ]]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

echo "ruff format を実行中..." >&2
uv run ruff format src tests >&2

echo "ruff check を実行中..." >&2
if ! uv run ruff check src tests >&2; then
  echo "ruff check でエラーが見つかりました。修正してください。" >&2
  exit 2
fi

# フォーマットで変更されたファイルを再ステージ
changed=$(git diff --name-only -- src/ tests/)
if [ -n "$changed" ]; then
  echo "フォーマットで変更されたファイルを再ステージ..." >&2
  echo "$changed" | xargs git add
fi
