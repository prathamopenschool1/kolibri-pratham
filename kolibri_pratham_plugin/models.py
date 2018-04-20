from jsonfield import JSONField
from django.db.models import ForeignKey

from kolibri.auth.models import AbstractFacilityDataModel
from kolibri.auth.models import Facility

class DataStore(AbstractFacilityDataModel):
    morango_model_name = "datastore"

    data = JSONField(default={}, blank=True)
    facility = ForeignKey(Facility)

    def infer_dataset(self, *args, **kwargs):
        return self.facility.dataset

    def calculate_partition(self):
        return self.dataset_id
