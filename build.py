from pybuilder.core import use_plugin, init, depends

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("python.sphinx")

name = "SRHPasswordManager"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on("cryptography")
    project.build_depends_on("mockito")
    
    project.set_property("coverage_break_build", True)
    project.set_property("coverage_threshold_warn", 50)
    project.set_property("coverage_fail_under", 50)

    project.set_property("sphinx_docroot", "docs")
    project.set_property("sphinx_source_dir", "docs/source")
    project.set_property("sphinx_output_dir", "docs/build/html")

@depends("generate_documentation")
def publish():
    pass
