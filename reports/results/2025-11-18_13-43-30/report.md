# Invenio Bugfix Verification Results

_Last updated: 2025-11-18 13:43:30 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 29 |
| **Patched Packages** | 15 |
| **Unpatched Packages** | 14 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 0 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 3 |
| ℹ️  No Change | 12 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/oarepo/pytest-invenio/tree/nested-db-session-rollback) | https://github.com/oarepo/pytest-invenio | nested-db-session-rollback |
| [invenio-files-rest](https://github.com/fenekku/invenio-files-res/tree/support_3.14) | https://github.com/fenekku/invenio-files-res | support_3.14 |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-files-rest` <br/> [original](packages/invenio-files-rest/test-output-original.txt) [patched](packages/invenio-files-rest/test-output-patched.txt) [warnings-patched](packages/invenio-files-rest/warnings-patched.md) | pytest-invenio | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-banners` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-rdm-records` | ⏭️  Skipped |
| `invenio-app-rdm` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-communities` | ⏭️  Skipped |
| `invenio-checks` | ⏭️  Skipped |
| `invenio-audit-logs` | ⏭️  Skipped |
| `invenio-administration` | ⏭️  Skipped |
| `invenio-records-resources` | ⏭️  Skipped |
| `invenio-github` | ⏭️  Skipped |
| `invenio-vocabularies` | ⏭️  Skipped |
| `invenio-search` | ⏭️  Skipped |
| `invenio-accounts` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-mail` <br/> [patched](packages/invenio-mail/test-output-patched.txt) [xml-patched](packages/invenio-mail/test-report-patched.xml) [warnings-patched](packages/invenio-mail/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-cache` <br/> [patched](packages/invenio-cache/test-output-patched.txt) [xml-patched](packages/invenio-cache/test-report-patched.xml) [warnings-patched](packages/invenio-cache/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-base` <br/> [patched](packages/invenio-base/test-output-patched.txt) [xml-patched](packages/invenio-base/test-report-patched.xml) [warnings-patched](packages/invenio-base/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-theme` <br/> [patched](packages/invenio-theme/test-output-patched.txt) [xml-patched](packages/invenio-theme/test-report-patched.xml) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-assets` <br/> [patched](packages/invenio-assets/test-output-patched.txt) [xml-patched](packages/invenio-assets/test-report-patched.xml) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-celery` <br/> [patched](packages/invenio-celery/test-output-patched.txt) [xml-patched](packages/invenio-celery/test-report-patched.xml) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-db` <br/> [patched](packages/invenio-db/test-output-patched.txt) [xml-patched](packages/invenio-db/test-report-patched.xml) [warnings-patched](packages/invenio-db/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-indexer` <br/> [patched](packages/invenio-indexer/test-output-patched.txt) [xml-patched](packages/invenio-indexer/test-report-patched.xml) [warnings-patched](packages/invenio-indexer/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-records-permissions` <br/> [patched](packages/invenio-records-permissions/test-output-patched.txt) [xml-patched](packages/invenio-records-permissions/test-report-patched.xml) [warnings-patched](packages/invenio-records-permissions/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-stats` <br/> [original](packages/invenio-stats/test-output-original.txt) [patched](packages/invenio-stats/test-output-patched.txt) [warnings-original](packages/invenio-stats/warnings-original.md) [warnings-patched](packages/invenio-stats/warnings-patched.md) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-records-files` <br/> [original](packages/invenio-records-files/test-output-original.txt) [patched](packages/invenio-records-files/test-output-patched.txt) | pytest-invenio invenio-files-rest | ❌ Fail | ❌ Fail | ⚠️ Tests still failing after patch |
| `invenio-sitemap` <br/> [patched](packages/invenio-sitemap/test-output-patched.txt) [xml-patched](packages/invenio-sitemap/test-report-patched.xml) [warnings-patched](packages/invenio-sitemap/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-jsonschemas` <br/> [patched](packages/invenio-jsonschemas/test-output-patched.txt) [xml-patched](packages/invenio-jsonschemas/test-report-patched.xml) [warnings-patched](packages/invenio-jsonschemas/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |
| `invenio-webhooks` <br/> [patched](packages/invenio-webhooks/test-output-patched.txt) [xml-patched](packages/invenio-webhooks/test-report-patched.xml) [warnings-patched](packages/invenio-webhooks/warnings-patched.md) | pytest-invenio | ⏭️  Skip | ✅ Pass | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 14 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 5 |
| `invenio-records-permissions` | 3 |
| `unknown` | 3 |
| `invenio-indexer` | 2 |
| `invenio-cache` | 1 |

#### Warning 2 - 8 occurrences

DeprecationWarning: ast.Str is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 8 |

#### Warning 3 - 7 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-indexer` | 2 |
| `invenio-records-permissions` | 2 |
| `unknown` | 2 |
| `invenio-jsonschemas` | 1 |

#### Warning 4 - 4 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-cache` | 1 |
| `invenio-records-permissions` | 1 |
| `invenio-sitemap` | 1 |
| `unknown` | 1 |

#### Warning 5 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 6 - 4 occurrences

SyntaxWarning: invalid escape sequence '\_'

| Package | Count |
|---------|-------|
| `invenio-mail` | 4 |

#### Warning 7 - 3 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |
| `invenio-webhooks` | 1 |
| `unknown` | 1 |

#### Warning 8 - 3 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |
| `invenio-records-permissions` | 1 |
| `unknown` | 1 |

#### Warning 9 - 3 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |
| `invenio-stats` | 1 |
| `unknown` | 1 |

#### Warning 10 - 3 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `unknown` | 3 |

#### Warning 11 - 3 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-indexer` | 2 |
| `unknown` | 1 |

#### Warning 12 - 3 occurrences

SyntaxWarning: invalid escape sequence '\*'

| Package | Count |
|---------|-------|
| `invenio-mail` | 3 |

#### Warning 13 - 2 occurrences

DeprecationWarning: 'pkgutil.get_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 2 |

#### Warning 14 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `unknown` | 2 |

#### Warning 15 - 2 occurrences

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-db` | 1 |
| `unknown` | 1 |

#### Warning 16 - 2 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |
| `unknown` | 1 |

#### Warning 17 - 2 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 2 |

#### Warning 18 - 2 occurrences

PytestConfigWarning: Unknown config option: pep8ignore

| Package | Count |
|---------|-------|
| `invenio-jsonschemas` | 1 |
| `unknown` | 1 |

#### Warning 19 - 2 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-files-rest` | 1 |
| `unknown` | 1 |

#### Warning 20 - 1 occurrence

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 21 - 1 occurrence

DeprecationWarning: 'pkgutil.find_loader' is deprecated and slated for removal in Python 3.14; use importlib.util.find_spec() instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: Attribute s is deprecated and will be removed in Python 3.14; use value instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 24 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 25 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 26 - 1 occurrence

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 27 - 1 occurrence

DeprecationWarning: Please use hash_password instead of encrypt_password.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 28 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 29 - 1 occurrence

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 30 - 1 occurrence

DeprecationWarning: ast.NameConstant is deprecated and will be removed in Python 3.14; use ast.Constant instead

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 31 - 1 occurrence

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 32 - 1 occurrence

PendingDeprecationWarning: The WSGI_PROXIES configuration is deprecated and it will be removed, use PROXYFIX_CONFIG instead

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 33 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 34 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 35 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 36 - 1 occurrence

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 37 - 1 occurrence

RuntimeWarning: Results are not stored in backend and should not be retrieved when task_always_eager is enabled, unless task_store_eager_result is enabled.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 38 - 1 occurrence

RuntimeWarning: You are overriding the default OAuthlib "URL encoded" set of valid characters. Make sure that the characters defined in oauthlib.common.urlencoded are indeed limitting your needs.

| Package | Count |
|---------|-------|
| `invenio-webhooks` | 1 |

#### Warning 39 - 1 occurrence

SADeprecationWarning: Query.values() is deprecated and will be removed in a future release.  Please use Query.with_entities() (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-indexer` | 1 |

#### Warning 40 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `unknown` | 1 |

#### Warning 41 - 1 occurrence

SyntaxWarning: "is" with 'str' literal. Did you mean "=="?

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 42 - 1 occurrence

SyntaxWarning: invalid escape sequence '\ '

| Package | Count |
|---------|-------|
| `invenio-mail` | 1 |

#### Warning 43 - 1 occurrence

UserWarning: Test

| Package | Count |
|---------|-------|
| `invenio-base` | 1 |

#### Warning 44 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `unknown` | 1 |


### Original

#### Warning 1 - 1 occurrence

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-stats` | 1 |




---

_For detailed test outputs and diffs, see the [full report](https://mesemus.github.io/invenio-bug-verification/)._