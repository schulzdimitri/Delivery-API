from abc import ABC, abstractmethod
from typing import Optional

class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_document(self, document: dict) -> dict: pass

    @abstractmethod
    def insert_list_of_documents(self, list_of_documents: list[dict]) -> None: pass
    
    @abstractmethod
    def select_many(self, doc_filter: dict = None) -> list[dict]: pass

    @abstractmethod
    def select_one(self, doc_filter: dict = None) -> dict: pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter: dict) -> list[dict]: pass

    @abstractmethod
    def select_if_property_exists(self, property_name: str) -> list[dict]: pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> dict: pass

    @abstractmethod
    def edit_registry(self, object_id: str, new_values: dict) -> None: pass
    
    @abstractmethod
    def edit_many_registries(self, doc_filter: dict, new_values: dict) -> None: pass
    
    @abstractmethod
    def edit_registry_with_increment(self, object_id: str, new_values: dict) -> None: pass