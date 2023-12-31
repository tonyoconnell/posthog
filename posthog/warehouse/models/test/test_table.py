from posthog.test.base import BaseTest
from posthog.warehouse.models import DataWarehouseTable, DataWarehouseCredential


class TestTable(BaseTest):
    # Not worth actually testing this as it would involve going to a remote server, and it's slow
    # def test_get_columns(self):
    #     credential = DataWarehouseCredential.objects.create(
    #         access_key='',
    #         access_secret='',
    #         team=self.team
    #     )
    #     table = DataWarehouseTable.objects.create(
    #         name='bla',
    #         url_pattern='https://databeach-hackathon.s3.amazonaws.com/tim_test/test_events6.pqt',
    #         credentials=credential,
    #         type=DataWarehouseTable.TableType.Parquet,
    #         team=self.team
    #     )
    #     table.get_columns()

    def test_hogql_definition(self):
        credential = DataWarehouseCredential.objects.create(access_key="test", access_secret="test", team=self.team)
        table = DataWarehouseTable.objects.create(
            name="bla",
            url_pattern="https://databeach-hackathon.s3.amazonaws.com/tim_test/test_events6.pqt",
            format=DataWarehouseTable.TableFormat.Parquet,
            team=self.team,
            columns={
                "id": "String",
                "timestamp": "DateTime64(3, 'UTC')",
                "mrr": "Nullable(Int64)",
                "offset": "UInt32",
            },
            credential=credential,
        )
        self.assertEqual(list(table.hogql_definition().fields.keys()), ["id", "timestamp", "mrr", "offset"])
