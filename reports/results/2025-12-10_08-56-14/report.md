# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-10 09:00:56 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 51 |
| **Patched Packages** | 1 |
| **Unpatched Packages** | 50 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 1 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [invenio-previewer](https://github.com/oarepo/invenio-previewer/tree/oarepo-feature-container-previewers) | https://github.com/oarepo/invenio-previewer | oarepo-feature-container-previewers |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-banners` | ⏭️  Skipped |
| `invenio-mail` | ⏭️  Skipped |
| `invenio-config` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-cache` | ⏭️  Skipped |
| `invenio-notifications` | ⏭️  Skipped |
| `invenio-base` | ⏭️  Skipped |
| `invenio-rdm-records` | ⏭️  Skipped |
| `invenio-app` | ⏭️  Skipped |
| `invenio-jobs` | ⏭️  Skipped |
| `invenio-theme` | ⏭️  Skipped |
| `invenio-assets` | ⏭️  Skipped |
| `invenio-celery` | ⏭️  Skipped |
| `invenio-pidstore` | ⏭️  Skipped |
| `invenio-db` | ⏭️  Skipped |
| `invenio-indexer` | ⏭️  Skipped |
| `invenio-oaiserver` | ⏭️  Skipped |
| `invenio-drafts-resources` | ⏭️  Skipped |
| `invenio-access` | ⏭️  Skipped |
| `invenio-rest` | ⏭️  Skipped |
| `invenio-requests` | ⏭️  Skipped |
| `invenio-pages` | ⏭️  Skipped |
| `invenio-records-permissions` | ⏭️  Skipped |
| `invenio-collections` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-stats` | ⏭️  Skipped |
| `invenio-userprofiles` | ⏭️  Skipped |
| `invenio-communities` | ⏭️  Skipped |
| `invenio-search-ui` | ⏭️  Skipped |
| `invenio-records-files` | ⏭️  Skipped |
| `invenio-logging` | ⏭️  Skipped |
| `invenio-sitemap` | ⏭️  Skipped |
| `invenio-files-rest` | ⏭️  Skipped |
| `invenio-formatter` | ⏭️  Skipped |
| `invenio-checks` | ⏭️  Skipped |
| `invenio-audit-logs` | ⏭️  Skipped |
| `invenio-records-rest` | ⏭️  Skipped |
| `invenio-administration` | ⏭️  Skipped |
| `invenio-records-resources` | ⏭️  Skipped |
| `invenio-github` | ⏭️  Skipped |
| `invenio-i18n` | ⏭️  Skipped |
| `invenio-oauth2server` | ⏭️  Skipped |
| `invenio-jsonschemas` | ⏭️  Skipped |
| `invenio-vocabularies` | ⏭️  Skipped |
| `invenio-search` | ⏭️  Skipped |
| `invenio-accounts` | ⏭️  Skipped |
| `invenio-users-resources` | ⏭️  Skipped |
| `invenio-webhooks` | ⏭️  Skipped |
| `invenio-records` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-app-rdm` | invenio-previewer | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-app-rdm/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-app-rdm/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-app-rdm/test-report-patched.xml)<br>[warnings](packages/invenio-app-rdm/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 14 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 14 |

#### Warning 2 - 6 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 6 |

#### Warning 3 - 6 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 6 |

#### Warning 4 - 3 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 3 |

#### Warning 5 - 2 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 2 |

#### Warning 6 - 2 occurrences

DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 2 |

#### Warning 7 - 2 occurrences

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 2 |

#### Warning 8 - 1 occurrence

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 9 - 1 occurrence

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 10 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 11 - 1 occurrence

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 12 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 13 - 1 occurrence

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 14 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 15 - 1 occurrence

DeprecationWarning: The '__version__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'importlib.metadata.version("marshmallow")' instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 16 - 1 occurrence

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 17 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_MAX_FILE_SIZE' is not set. In future, please set it explicitly to define your max file size, or be aware that the default value used i.e. FILES_REST_DEFAULT_MAX_FILE_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 18 - 1 occurrence

DeprecationWarning: The configuration value 'RDM_FILES_DEFAULT_QUOTA_SIZE' is not set. In future, please set it explicitly to define your quota size, or be aware that the default value used i.e. FILES_REST_DEFAULT_QUOTA_SIZE will be 10 * (10**9) (10 GB).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 19 - 1 occurrence

DeprecationWarning: `es_clear` fixture is deprecated, use `search_clear` instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 20 - 1 occurrence

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 21 - 1 occurrence

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: subject_nested is deprecated. Use subject_combined instead.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 23 - 1 occurrence

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |

#### Warning 24 - 1 occurrence

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-app-rdm` | 1 |




---