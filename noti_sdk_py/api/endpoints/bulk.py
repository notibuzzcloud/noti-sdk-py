"""Bulk messaging endpoints for NotiBuzz SDK."""

from typing import Any, Dict, List, Optional
from urllib.parse import quote

from ..client import get_client


def _make_path(template: str, params: Optional[Dict[str, Any]] = None) -> str:
    """Replace path parameters in template with actual values."""
    if not params:
        return template
    result = template
    for key, value in params.items():
        result = result.replace(f"{{{key}}}", quote(str(value)))
    return result


def list_bulk_jobs(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
) -> Any:
    """
    List bulk messaging jobs (waiting, delayed, active).

    Method: GET
    Path: /api/bulk/jobs

    Returns:
        Object with ok, jobs list, and total.
    """
    path = _make_path("/api/bulk/jobs", path_params)
    return get_client().get(path, query)


def pause_bulk_job(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
) -> Any:
    """
    Pause a bulk job by jobId.

    Method: POST
    Path: /api/bulk/jobs/{jobId}/pause

    Args:
        path_params: Must include 'jobId'.

    Returns:
        Result with ok, jobId, paused, pausedAt, keysTTLSeconds.
    """
    path = _make_path("/api/bulk/jobs/{jobId}/pause", path_params)
    return get_client().post(path, body)


def resume_bulk_job(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
) -> Any:
    """
    Resume a paused bulk job.

    Method: POST
    Path: /api/bulk/jobs/{jobId}/resume

    Args:
        path_params: Must include 'jobId'.

    Returns:
        Result with ok, jobId, resumed.
    """
    path = _make_path("/api/bulk/jobs/{jobId}/resume", path_params)
    return get_client().post(path, body)


def cancel_bulk_job(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Any] = None,
) -> Any:
    """
    Cancel a bulk job.

    Method: POST
    Path: /api/bulk/jobs/{jobId}/cancel

    Args:
        path_params: Must include 'jobId'.

    Returns:
        Result with ok, jobId, removed, cancelKeySet, keysTTLSeconds.
    """
    path = _make_path("/api/bulk/jobs/{jobId}/cancel", path_params)
    return get_client().post(path, body)


def bulk_stop_campaign(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, List[str]]] = None,
) -> Any:
    """
    Stop a bulk messaging campaign in progress.
    
    Method: POST
    Path: /api/bulk/campaigns/{id}/stop
    
    Args:
        path_params: Path parameters (must include 'id').
        query: Query parameters.
        body: Request body (e.g., {'sessions': ['default']}).
        
    Returns:
        Stop campaign result.
    """
    path = _make_path("/api/bulk/campaigns/{id}/stop", path_params)
    return get_client().post(path, body)


def bulk_resume_campaign(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, Any]] = None,
    body: Optional[Dict[str, List[str]]] = None,
) -> Any:
    """
    Resume a previously stopped bulk messaging campaign.
    
    Method: POST
    Path: /api/bulk/campaigns/{id}/resume
    
    Args:
        path_params: Path parameters (must include 'id').
        query: Query parameters.
        body: Request body (e.g., {'sessions': ['default']}).
        
    Returns:
        Resume campaign result.
    """
    path = _make_path("/api/bulk/campaigns/{id}/resume", path_params)
    return get_client().post(path, body)


def bulk_availability(
    path_params: Optional[Dict[str, Any]] = None,
    query: Optional[Dict[str, str]] = None,
    body: Optional[Any] = None,
) -> Any:
    """
    Check availability of capacity for bulk messaging.
    Returns information about current and maximum capacity for parallel sends.
    
    Method: GET
    Path: /api/bulk/availability
    
    Args:
        path_params: Path parameters (not used for this endpoint).
        query: Query parameters (e.g., {'requester': 'my-app'}).
        body: Request body (not used for GET).
        
    Returns:
        Availability information with available, current, max, origin, and requester fields.
    """
    path = _make_path("/api/bulk/availability", path_params)
    return get_client().get(path, query)

