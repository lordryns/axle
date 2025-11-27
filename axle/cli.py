import os
import subprocess

import click
import platformdirs


def get_config_path() -> str:
    config_home = platformdirs.user_config_dir(ensure_exists=True)
    return os.path.join(config_home, "axle")


def get_template_path() -> str:
    return os.path.join(get_config_path(), "templates")


def scan_template_path() -> list[str]:
    return os.listdir(get_template_path())


def copy_template_to_path(cur_file: str, dest: str) -> bool:
    try:
        with open(os.path.join(get_template_path(), dest), "w") as f:
            with open(cur_file, "r") as c:
                f.write(c.read())

        return True
    except Exception:
        # python io operations fail right?
        return False


@click.group()
def cli():
    pass


@cli.command(help="List all available templates")
def list():
    click.echo("Listing templates...")


@cli.command(help="Use this to store a template")
@click.argument("name")
def store(name):
    if name.split(".")[-1] != "py":
        click.echo(click.style("template must be a .py file!", fg="red"))
        return

    if not os.path.exists(name):
        click.echo(
            click.style(
                f"File does not exist at location: {os.path.abspath(name)}", fg="red"
            )
        )
        return

    if name in scan_template_path():
        click.echo(
            click.style(
                "A template with this name already exists, do you want to replace it?",
                fg="yellow",
            )
        )

        if not click.confirm("Replace?"):
            click.echo(click.style("Operation aborted by user", fg="red"))
            return

    else:
        click.echo(click.style("OK", fg="blue"))

    copy_template_to_path(name, name)
    if click.confirm("Delete original on disk?"):
        os.remove(name)
        click.echo(click.style("Done!", fg="green"))
    else:
        click.echo(click.style("No!", fg="blue"))

    tname = os.path.split(name)[-1].split(".")[-2]
    click.echo(click.style(f"Template ({tname}) added successfully!", fg="green"))


@cli.command(help="Use this to permanently delete a template")
def remove():
    click.echo("Deleting template...")


@cli.command(help="Generate scaffold based on template")
@click.argument("template")
@click.argument("path")
def use(template, path):
    template_path = os.path.join(get_template_path(), template + ".py")
    if not os.path.exists(template_path):
        click.echo(click.style("Template does not exist!", fg="red"))
        return

    click.echo(click.style(f"Creating {path} using {template}", fg="blue"))
    subprocess.run(["python", os.path.abspath(template_path)])


def main():
    if not os.path.exists(get_template_path()):
        os.makedirs(get_template_path())
    cli()


if __name__ == "__main__":
    main()
