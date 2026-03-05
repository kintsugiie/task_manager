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

if __name__ == "__main__":
    cli()


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
