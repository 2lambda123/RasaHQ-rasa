import pytest
import shutil
from _pytest.tmpdir import TempdirFactory

from rasa.cli import scaffold
from rasa.core.agent import Agent
from rasa.core.processor import MessageProcessor


@pytest.fixture(scope="session")
def simple_project(tmpdir_factory: TempdirFactory):
    path = tmpdir_factory.mktemp("simple")
    scaffold.create_initial_project(str(path))
    return path


@pytest.fixture(scope="session")
def formbot_project(tmpdir_factory: TempdirFactory):
    path = tmpdir_factory.mktemp("formbot") / "content"
    shutil.copytree("examples/formbot", path)
    return path


@pytest.fixture
async def default_processor(default_agent: Agent) -> MessageProcessor:
    return default_agent.processor
