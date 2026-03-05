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
@click.argument('title')
def add(title):
    """Добавить задачу"""
    from utils import load_tasks, save_tasks

    tasks = load_tasks()
    tasks.append({'title': title, 'done': False})
    save_tasks(tasks)

    console.print(f"[green]✅ Добавлена задача: {title}[/green]")


if __name__ == "__main__":
    cli()
