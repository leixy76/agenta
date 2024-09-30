# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..core.pydantic_utilities import parse_obj_as
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.create_span import CreateSpan
from ..types.create_trace_response import CreateTraceResponse
from ..types.with_pagination import WithPagination
from ..types.trace_detail import TraceDetail
from ..core.jsonable_encoder import jsonable_encoder
from ..types.span_detail import SpanDetail
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ObservabilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def dashboard(
        self,
        *,
        app_id: str,
        time_range: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        variant: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        app_id : str

        time_range : typing.Optional[str]

        environment : typing.Optional[str]

        variant : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.dashboard(
            app_id="app_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "observability/dashboard/",
            method="GET",
            params={
                "app_id": app_id,
                "timeRange": time_range,
                "environment": environment,
                "variant": variant,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_traces(
        self,
        *,
        trace: str,
        spans: typing.Sequence[CreateSpan],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTraceResponse:
        """
        Parameters
        ----------
        trace : str

        spans : typing.Sequence[CreateSpan]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTraceResponse
            Successful Response

        Examples
        --------
        import datetime

        from agenta import AgentaApi, CreateSpan

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.create_traces(
            trace="trace",
            spans=[
                CreateSpan(
                    id="id",
                    app_id="app_id",
                    name="name",
                    spankind="spankind",
                    status="status",
                    start_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    end_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "observability/trace/",
            method="POST",
            json={
                "trace": trace,
                "spans": spans,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CreateTraceResponse,
                    parse_obj_as(
                        type_=CreateTraceResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_traces(
        self,
        *,
        app_id: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        variant: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WithPagination:
        """
        Parameters
        ----------
        app_id : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        environment : typing.Optional[str]

        variant : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WithPagination
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.get_traces(
            app_id="app_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "observability/traces/",
            method="GET",
            params={
                "app_id": app_id,
                "page": page,
                "pageSize": page_size,
                "type": type,
                "trace_id": trace_id,
                "environment": environment,
                "variant": variant,
                "created_at": created_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WithPagination,
                    parse_obj_as(
                        type_=WithPagination,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_traces(
        self,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.delete_traces(
            request=["string"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "observability/traces/",
            method="DELETE",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_trace_detail(
        self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TraceDetail:
        """
        Parameters
        ----------
        trace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceDetail
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.get_trace_detail(
            trace_id="trace_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"observability/traces/{jsonable_encoder(trace_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TraceDetail,
                    parse_obj_as(
                        type_=TraceDetail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_spans_of_generation(
        self,
        *,
        app_id: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        variant: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        app_id : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        environment : typing.Optional[str]

        variant : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.get_spans_of_generation(
            app_id="app_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "observability/spans/",
            method="GET",
            params={
                "app_id": app_id,
                "page": page,
                "pageSize": page_size,
                "type": type,
                "trace_id": trace_id,
                "environment": environment,
                "variant": variant,
                "created_at": created_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_spans_of_trace(
        self,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.delete_spans_of_trace(
            request=["string"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "observability/spans/",
            method="DELETE",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_span_of_generation(
        self,
        span_id: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanDetail:
        """
        Parameters
        ----------
        span_id : str

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanDetail
            Successful Response

        Examples
        --------
        from agenta import AgentaApi

        client = AgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.observability.get_span_of_generation(
            span_id="span_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"observability/spans/{jsonable_encoder(span_id)}/",
            method="GET",
            params={
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SpanDetail,
                    parse_obj_as(
                        type_=SpanDetail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncObservabilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def dashboard(
        self,
        *,
        app_id: str,
        time_range: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        variant: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        app_id : str

        time_range : typing.Optional[str]

        environment : typing.Optional[str]

        variant : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.dashboard(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observability/dashboard/",
            method="GET",
            params={
                "app_id": app_id,
                "timeRange": time_range,
                "environment": environment,
                "variant": variant,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_traces(
        self,
        *,
        trace: str,
        spans: typing.Sequence[CreateSpan],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTraceResponse:
        """
        Parameters
        ----------
        trace : str

        spans : typing.Sequence[CreateSpan]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTraceResponse
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from agenta import AsyncAgentaApi, CreateSpan

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.create_traces(
                trace="trace",
                spans=[
                    CreateSpan(
                        id="id",
                        app_id="app_id",
                        name="name",
                        spankind="spankind",
                        status="status",
                        start_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                        end_time=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observability/trace/",
            method="POST",
            json={
                "trace": trace,
                "spans": spans,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CreateTraceResponse,
                    parse_obj_as(
                        type_=CreateTraceResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_traces(
        self,
        *,
        app_id: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        variant: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WithPagination:
        """
        Parameters
        ----------
        app_id : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        environment : typing.Optional[str]

        variant : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WithPagination
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.get_traces(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observability/traces/",
            method="GET",
            params={
                "app_id": app_id,
                "page": page,
                "pageSize": page_size,
                "type": type,
                "trace_id": trace_id,
                "environment": environment,
                "variant": variant,
                "created_at": created_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WithPagination,
                    parse_obj_as(
                        type_=WithPagination,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_traces(
        self,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.delete_traces(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observability/traces/",
            method="DELETE",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_trace_detail(
        self, trace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TraceDetail:
        """
        Parameters
        ----------
        trace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TraceDetail
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.get_trace_detail(
                trace_id="trace_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"observability/traces/{jsonable_encoder(trace_id)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    TraceDetail,
                    parse_obj_as(
                        type_=TraceDetail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_spans_of_generation(
        self,
        *,
        app_id: str,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
        variant: typing.Optional[str] = None,
        created_at: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.Any]:
        """
        Parameters
        ----------
        app_id : str

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        type : typing.Optional[str]

        trace_id : typing.Optional[str]

        environment : typing.Optional[str]

        variant : typing.Optional[str]

        created_at : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.get_spans_of_generation(
                app_id="app_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observability/spans/",
            method="GET",
            params={
                "app_id": app_id,
                "page": page,
                "pageSize": page_size,
                "type": type,
                "trace_id": trace_id,
                "environment": environment,
                "variant": variant,
                "created_at": created_at,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.Optional[typing.Any],
                    parse_obj_as(
                        type_=typing.Optional[typing.Any],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_spans_of_trace(
        self,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.delete_spans_of_trace(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "observability/spans/",
            method="DELETE",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_span_of_generation(
        self,
        span_id: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SpanDetail:
        """
        Parameters
        ----------
        span_id : str

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SpanDetail
            Successful Response

        Examples
        --------
        import asyncio

        from agenta import AsyncAgentaApi

        client = AsyncAgentaApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.observability.get_span_of_generation(
                span_id="span_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"observability/spans/{jsonable_encoder(span_id)}/",
            method="GET",
            params={
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SpanDetail,
                    parse_obj_as(
                        type_=SpanDetail,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)