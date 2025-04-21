install: #команда для первого клонирование репозитория или после удаления зависимостей
	uv sync

brain-games: #запуск программы простой командой
	uv run brain-games

build: #сборка проекта
	uv build

package-install: #установка пакета
	uv tool install dist/*.whl