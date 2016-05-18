# datadog_logger
rh_logger plugin for datadog

This package logs to Datadog (https://app.datadoghq.com) on behalf
of the rh_logger package. To use:

* pip install .
* Set the RH_LOGGING_BACKEND environment variable to "datadog"
* Set the RH_DATADOG_API_KEY environment variable to your datadog API key
* Set the RH_DATADOG_APP_KEY environment variable to your datadog app key
* Use 'rh_logger.get_logger()' to get yourself a logger and log away.