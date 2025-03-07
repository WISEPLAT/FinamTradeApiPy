from typing import Union

from finam_trade_api.base_client import BaseClient
from finam_trade_api.exceptions import FinamTradeApiError
from finam_trade_api.models import ErrorBodyModel
from finam_trade_api.order.model import (
    CreateOrderRequestModel,
    CreateOrderResponseModel,
    CreateStopOrderRequestModel,
    CreateStopOrderResponseModel,
    DelOrderModel,
    DelOrderResponseModel,
    DelStopOrderRequestModel
)
from finam_trade_api.order.model import \
    DelStopOrderResponseModel as DelStopOrderResponse
from finam_trade_api.order.model import (
    OrdersRequestModel,
    OrdersResponseModel,
    StopOrdersResponseModel
)


class OrderClient(BaseClient):
    def __init__(self, token: str):
        super().__init__(token)
        self._order_url = "/api/v1/orders"
        self._stop_order_url = "/api/v1/stops"

    async def get_orders(self, params: OrdersRequestModel) -> Union[OrdersResponseModel, ErrorBodyModel]:
        response, ok = await self._exec_request(
            self.RequestMethod.GET,
            self._order_url,
            params=params.dict(exclude_none=True)
        )
        if not ok:
            err = ErrorBodyModel(**response)
            raise FinamTradeApiError(f"{err.error.code} | {err.error.data} | {err.error.message}")
        return OrdersResponseModel(**response)

    async def create_order(self, payload: CreateOrderRequestModel) -> Union[CreateOrderResponseModel, ErrorBodyModel]:
        response, ok = await self._exec_request(
            self.RequestMethod.POST,
            self._order_url,
            payload.dict(exclude_none=True)
        )
        if not ok:
            err = ErrorBodyModel(**response)
            raise FinamTradeApiError(f"{err.error.code} | {err.error.data} | {err.error.message}")
        return CreateOrderResponseModel(**response)

    async def del_order(self, params: DelOrderModel) -> Union[DelOrderResponseModel, ErrorBodyModel]:
        response, ok = await self._exec_request(
            self.RequestMethod.DELETE,
            self._order_url,
            params=params.dict()
        )
        if not ok:
            err = ErrorBodyModel(**response)
            raise FinamTradeApiError(f"{err.error.code} | {err.error.data} | {err.error.message}")
        return DelOrderResponseModel(**response)

    async def get_stop_orders(self, params: OrdersRequestModel) -> Union[StopOrdersResponseModel, ErrorBodyModel]:
        response, ok = await self._exec_request(
            self.RequestMethod.GET,
            self._stop_order_url,
            params.dict(exclude_none=True)
        )
        if not ok:
            err = ErrorBodyModel(**response)
            raise FinamTradeApiError(f"{err.error.code} | {err.error.data} | {err.error.message}")
        return StopOrdersResponseModel(**response)

    async def create_stop_order(
            self,
            payload: CreateStopOrderRequestModel
    ) -> Union[CreateStopOrderResponseModel, ErrorBodyModel]:
        response, ok = await self._exec_request(
            self.RequestMethod.POST,
            self._stop_order_url,
            payload.dict(exclude_none=True)
        )
        if not ok:
            err = ErrorBodyModel(**response)
            raise FinamTradeApiError(f"{err.error.code} | {err.error.data} | {err.error.message}")
        return CreateStopOrderResponseModel(**response)

    async def del_stop_order(self, params: DelStopOrderRequestModel) -> Union[DelStopOrderResponse, ErrorBodyModel]:
        response, ok = await self._exec_request(
            self.RequestMethod.DELETE,
            self._stop_order_url,
            params.dict()
        )
        if not ok:
            err = ErrorBodyModel(**response)
            raise FinamTradeApiError(f"{err.error.code} | {err.error.data} | {err.error.message}")
        return DelStopOrderResponse(**response)
