# ------------------------------------------------------------------------------
# PyCOMPSs App
# ------------------------------------------------------------------------------
from .. import App
from pycompss.api.api import compss_wait_on


class PyCOMPSsApp(App):
    """
    PyCOMPSsApp: uses PyCOMPSs.
    """

    def _post_run(self, tool_instance, output_files, output_metadata):
        """
        Adds a wait command to ensure asynchronous tasks are
        terminated before unstaging.
        """
        output_files, output_metadata = super(PyCOMPSsApp, self)._post_run(
            tool_instance, output_files, output_metadata)
        print "pycompss _post_run"
        output_files = compss_wait_on(output_files)
        return output_files, output_metadata
