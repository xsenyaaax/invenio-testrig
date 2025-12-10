## Collected Warnings

### Patched

#### Warning 1 - 15 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-userprofiles` | 5 |
| `invenio-records-permissions` | 3 |
| `invenio-indexer` | 2 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |
| `invenio-rest` | 1 |

#### Warning 2 - 7 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-indexer` | 2 |
| `invenio-notifications` | 2 |
| `invenio-records-permissions` | 2 |
| `invenio-jsonschemas` | 1 |

#### Warning 3 - 4 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-notifications` | 1 |
| `invenio-pidstore` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-userprofiles` | 1 |

#### Warning 4 - 4 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-cache` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-sitemap` | 1 |

#### Warning 5 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 6 - 3 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |
| `invenio-notifications` | 1 |
| `invenio-records-permissions` | 1 |

#### Warning 7 - 3 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-rest` | 2 |
| `invenio-records-permissions` | 1 |

#### Warning 8 - 3 occurrences

PendingDeprecationWarning: Schema().dump().data and Schema().dump().errors as well as Schema().load().data and Schema().loads().dataattributes are deprecated in marshmallow v3.x.

| Package | Count |
|---------|-------|
| `invenio-rest` | 3 |

#### Warning 9 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-notifications` | 2 |

#### Warning 10 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-notifications` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 11 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 12 - 2 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-indexer` | 2 |

#### Warning 13 - 2 occurrences

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-config` | 1 |

#### Warning 14 - 2 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-notifications` | 1 |
| `invenio-pidstore` | 1 |

#### Warning 15 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 16 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 17 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-notifications` | 1 |

#### Warning 18 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 19 - 1 occurrence

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-notifications` | 1 |

#### Warning 20 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-db` | 1 |

#### Warning 21 - 1 occurrence

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-notifications` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: current_userprofile is deprecated, use current_user instead

| Package | Count |
|---------|-------|
| `invenio-userprofiles` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-userprofiles` | 1 |

#### Warning 25 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 26 - 1 occurrence

PendingDeprecationWarning: This feature is deprecated.

| Package | Count |
|---------|-------|
| `invenio-logging` | 1 |

#### Warning 27 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 28 - 1 occurrence

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |

#### Warning 29 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 30 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 31 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |


