from typing import Type, Union, Dict, Any

from s4ap.modinfo import ModInfo
from s4ap.persistance.ap_data_manager import S4APDataManager
from sims4communitylib.persistence.data_management.common_data_manager_registry import CommonDataManagerRegistry
from sims4communitylib.persistence.data_stores.common_data_store import CommonDataStore
from sims4communitylib.services.common_service import CommonService


class S4APDataManagerUtils(CommonService):
    """ Utilities for accessing data stores """

    def __init__(self) -> None:
        self._data_manager: S4APDataManager = None

    @property
    def data_manager(self) -> S4APDataManager:
        """ The data manager containing data. """
        if self._data_manager is None:
            # We locate the data manager by using the Mod Identity of our Mod. This should match the Mod Identity we specified in the "mod_identity" property of the Data Manager.
            self._data_manager: S4APDataManager = CommonDataManagerRegistry().locate_data_manager(
                ModInfo.get_identity())
        return self._data_manager

    # We will discuss this function a bit later in the tutorial!
    def _get_data_store(self, data_store_type: Type[CommonDataStore]) -> Union[CommonDataStore, None]:
        return self.data_manager.get_data_store_by_type(data_store_type)

    def get_all_data(self) -> Dict[str, Dict[str, Any]]:
        """ Get all data. """
        return self.data_manager._data_store_data

    def save(self) -> bool:
        """ Save data. """
        return self.data_manager.save()

    def reset(self, prevent_save: bool = False) -> bool:
        """ Reset data. """
        return self.data_manager.remove_all_data(prevent_save=prevent_save)