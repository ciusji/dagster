# pylint: disable=redefined-outer-name
# start_marker
from dagster import AssetGroup, asset
from dagster_aws.s3 import s3_pickle_asset_io_manager, s3_resource


@asset
def upstream_asset():
    return [1, 2, 3]


@asset
def downstream_asset(upstream_asset):
    return upstream_asset + [4]


asset_group = AssetGroup(
    [upstream_asset, downstream_asset],
    resource_defs={"io_manager": s3_pickle_asset_io_manager, "s3": s3_resource},
)

# end_marker
