from software_defined_assets.spark_weather_assets_group import spark_weather_assets

from dagster import repository


@repository
def software_defined_assets():
    return [spark_weather_assets]
