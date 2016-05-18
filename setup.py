import setuptools

setuptools.setup(
    description="Logging and metric reporting for Rhoana pipeline via datadog",
    depenendency_links= [
        "https://github.com/Rhoana/rh_logger/archive/0.1.0.tar.gz#egg=rh_logger-0.1.0"
    ],
    entry_points={
        "rh_logger.backend": {
            "datadog = datadog_logger:get_logger"
        }
    },
    install_requires=[
        "datadog>=0.11.0"
    ],
    name="datadog_logger",
    packages=["datadog_logger"],
    url="https://github.com/Rhoana/datadog_logger",
    version="0.1.0"
)
