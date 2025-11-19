# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-11-19 14:40:23 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 10 |
| **Patched Packages** | 10 |
| **Unpatched Packages** | 0 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 10 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [pytest-invenio](https://github.com/oarepo/pytest-invenio/tree/nested-db-session-rollback) | https://github.com/oarepo/pytest-invenio | nested-db-session-rollback |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-mail` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-mail/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-mail/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-mail/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-queues` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-queues/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-queues/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-queues/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-cache` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-cache/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-cache/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-cache/test-report-patched.xml)<br>[warnings](packages/invenio-cache/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-app` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app/test-report-patched.xml)<br>[warnings](packages/invenio-app/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-theme` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-theme/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-theme/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-theme/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-assets` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-assets/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-assets/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-assets/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-celery` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-celery/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-celery/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-celery/test-report-patched.xml) | ✅ Patch applied successfully, tests passed |
| `invenio-pidstore` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pidstore/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pidstore/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pidstore/test-report-patched.xml)<br>[warnings](packages/invenio-pidstore/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-records-permissions` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-records-permissions/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-records-permissions/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-records-permissions/test-report-patched.xml)<br>[warnings](packages/invenio-records-permissions/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-formatter` | pytest-invenio | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-formatter/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-formatter/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-formatter/test-report-patched.xml)<br>[warnings](packages/invenio-formatter/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 7 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 3 |
| `invenio-pidstore` | 2 |
| `invenio-cache` | 1 |
| `invenio-formatter` | 1 |

#### Warning 2 - 4 occurrences

PytestMockWarning: Mocks returned by pytest-mock do not need to be used as context managers. The mocker fixture automatically undoes mocking at the end of a test. This warning can be ignored if it was triggered by mocking a context manager. https://pytest-mock.readthedocs.io/en/latest/usage.html#usage-as-context-manager

| Package | Count |
|---------|-------|
| `invenio-cache` | 4 |

#### Warning 3 - 3 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |
| `invenio-cache` | 1 |
| `invenio-records-permissions` | 1 |

#### Warning 4 - 2 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |
| `invenio-records-permissions` | 1 |

#### Warning 5 - 2 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 2 |

#### Warning 6 - 2 occurrences

PytestDeprecationWarning: @pytest.yield_fixture is deprecated.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 2 |

#### Warning 7 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 8 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('flask_admin.contrib')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 9 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 10 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |

#### Warning 11 - 1 occurrence

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 12 - 1 occurrence

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 13 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestPermissionPolicy' because it has a __init__ constructor (from: tests/test_permissions_base.py)

| Package | Count |
|---------|-------|
| `invenio-records-permissions` | 1 |

#### Warning 14 - 1 occurrence

UserWarning: Set configuration variable SECRET_KEY with random string

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 15 - 1 occurrence

UserWarning: Using the in-memory storage for tracking rate limits as no storage was explicitly specified. This is not recommended for production use. See: https://flask-limiter.readthedocs.io#configuring-a-storage-backend for documentation about configuring the storage backend.

| Package | Count |
|---------|-------|
| `invenio-app` | 1 |

#### Warning 16 - 1 occurrence

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-pidstore` | 1 |




---