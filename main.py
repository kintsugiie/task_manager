#!/usr/bin/env python3
"""Простой менеджер задач CLI"""

import click
from rich.console import Console
from rich.table import Table

console = Console()

@click.group()
def cli():
    """Менеджер задач"""
    pass

@cli.command()
def list():
    """Показать все задачи"""
    click.echo("Список задач (пока пусто)")



@cli.command()
def list():
    """Показать все задачи"""
    from utils import load_tasks

    tasks = load_tasks()
    if not tasks:
        console.print("[yellow]Задач нет[/yellow]")
        return

    table = Table(title="Список задач")
    table.add_column("ID")
    table.add_column("Задача")
    table.add_column("Статус")

    for i, task in enumerate(tasks, 1):
        status = "✅" if task.get('done') else "⏳"
        table.add_row(str(i), task['title'], status)

    console.print(table)


@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Отметить задачу выполненной"""
    from utils import load_tasks, save_tasks

    tasks = load_tasks()
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]['done'] = True
        save_tasks(tasks)
        console.print(f"[green]✅ Задача {task_id} отмечена выполненной[/green]")
    else:
        console.print(f"[red]❌ Задача {task_id} не найдена[/red]")


if __name__ == "__main__":
    cli()