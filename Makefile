install: #команда для первого клонирование репозитория или после удаления зависимостей
	uv sync

brain-games: #запуск программы простой командой
	uv run brain-games

build: #сборка проекта
	uv build

package-install: #установка пакета
	uv tool install dist/*.whl

lint: #проверка линтером ruff на соответствие стандартам
	uv run ruff check brain_games

package-reinstall: #переустановка пакета после обновления
	uv tool install --force dist/*whl