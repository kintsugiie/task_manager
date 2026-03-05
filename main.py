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
