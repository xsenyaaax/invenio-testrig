# Invenio Bugfix Verification Results

> **⏳ Status: Running** - This report is being updated as tests complete.

_Last updated: 2025-12-11 12:49:40 UTC_

## 📊 Overall Status

| Metric | Count |
|--------|-------|
| **Total Packages** | 43 |
| **Patched Packages** | 9 |
| **Unpatched Packages** | 34 |

### Patch Results
| Result | Count |
|--------|-------|
| ✅ Fixed | 9 |
| ❌ Regressions | 0 |
| ⚠️  Still Failing | 0 |
| ℹ️  No Change | 0 |

## 🔧 Configured Patches

| Patched Package | Repository | Branch |
|----------------|------------|--------|
| [invenio-previewer](https://github.com/oarepo/invenio-previewer/tree/oarepo-feature-container-previewers) | https://github.com/oarepo/invenio-previewer | oarepo-feature-container-previewers |
| [invenio-records-resources](https://github.com/oarepo/invenio-records-resources/tree/oarepo-feature-extractors) | https://github.com/oarepo/invenio-records-resources | oarepo-feature-extractors |
| [invenio-rdm-records](https://github.com/oarepo/invenio-rdm-records/tree/oarepo-feature-zip) | https://github.com/oarepo/invenio-rdm-records | oarepo-feature-zip |
| [invenio-app-rdm](https://github.com/oarepo/invenio-app-rdm/tree/oarepo-feature-extract-preview-ui-links) | https://github.com/oarepo/invenio-app-rdm | oarepo-feature-extract-preview-ui-links |

## 🔄 Patched Packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|

## 📦 Packages that do not depend on patched packages

| Package | Build Status |
|---------|--------------|
| `invenio-mail` | ⏭️  Skipped |
| `invenio-config` | ⏭️  Skipped |
| `invenio-queues` | ⏭️  Skipped |
| `invenio-oauthclient` | ⏭️  Skipped |
| `invenio-cache` | ⏭️  Skipped |
| `invenio-base` | ⏭️  Skipped |
| `invenio-app` | ⏭️  Skipped |
| `invenio-theme` | ⏭️  Skipped |
| `invenio-assets` | ⏭️  Skipped |
| `invenio-celery` | ⏭️  Skipped |
| `invenio-pidstore` | ⏭️  Skipped |
| `invenio-db` | ⏭️  Skipped |
| `invenio-indexer` | ⏭️  Skipped |
| `invenio-oaiserver` | ⏭️  Skipped |
| `invenio-access` | ⏭️  Skipped |
| `invenio-rest` | ⏭️  Skipped |
| `invenio-records-permissions` | ⏭️  Skipped |
| `invenio-records-ui` | ⏭️  Skipped |
| `invenio-stats` | ⏭️  Skipped |
| `invenio-userprofiles` | ⏭️  Skipped |
| `invenio-search-ui` | ⏭️  Skipped |
| `invenio-records-files` | ⏭️  Skipped |
| `invenio-logging` | ⏭️  Skipped |
| `invenio-sitemap` | ⏭️  Skipped |
| `invenio-files-rest` | ⏭️  Skipped |
| `invenio-formatter` | ⏭️  Skipped |
| `invenio-records-rest` | ⏭️  Skipped |
| `invenio-i18n` | ⏭️  Skipped |
| `invenio-oauth2server` | ⏭️  Skipped |
| `invenio-jsonschemas` | ⏭️  Skipped |
| `invenio-search` | ⏭️  Skipped |
| `invenio-accounts` | ⏭️  Skipped |
| `invenio-webhooks` | ⏭️  Skipped |
| `invenio-records` | ⏭️  Skipped |

## 🔄 Packages that depend on patched packages

| Package | Patches Applied | Original | Patched | Result |
|---------|----------------|--------|-------|--------|
| `invenio-banners` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-banners/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-banners/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-banners/test-report-patched.xml)<br>[warnings](packages/invenio-banners/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-notifications` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-notifications/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-notifications/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-notifications/test-report-patched.xml)<br>[warnings](packages/invenio-notifications/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-jobs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-jobs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-jobs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-jobs/test-report-patched.xml)<br>[warnings](packages/invenio-jobs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-drafts-resources` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-drafts-resources/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-drafts-resources/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-drafts-resources/test-report-patched.xml)<br>[warnings](packages/invenio-drafts-resources/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-pages` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-pages/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-pages/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-pages/test-report-patched.xml)<br>[warnings](packages/invenio-pages/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-checks` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-checks/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-checks/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-checks/test-report-patched.xml)<br>[warnings](packages/invenio-checks/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-audit-logs` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-audit-logs/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-audit-logs/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-audit-logs/test-report-patched.xml)<br>[warnings](packages/invenio-audit-logs/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-administration` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-administration/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-administration/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-administration/test-report-patched.xml)<br>[warnings](packages/invenio-administration/warnings-patched.md) | ✅ Patch applied successfully, tests passed |
| `invenio-github` | invenio-records-resources | ⏭️  Skip | ✅ Pass<br>[output](packages/invenio-github/test-output-patched.txt)<br>[output-no-warnings](packages/invenio-github/test-output-no-warnings-patched.txt)<br>[xml](packages/invenio-github/test-report-patched.xml)<br>[warnings](packages/invenio-github/warnings-patched.md) | ✅ Patch applied successfully, tests passed |

## Collected Warnings

### Patched

#### Warning 1 - 41 occurrences

DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 7 |
| `invenio-jobs` | 7 |
| `invenio-audit-logs` | 6 |
| `invenio-banners` | 6 |
| `invenio-github` | 6 |
| `invenio-pages` | 6 |
| `invenio-administration` | 3 |

#### Warning 2 - 16 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |

#### Warning 3 - 16 occurrences

DeprecationWarning: jsonschema.RefResolver is deprecated as of v4.18.0, in favor of the https://github.com/python-jsonschema/referencing library, which provides more compliant referencing behavior as well as more flexible APIs for customization. A future release will remove RefResolver. Please file a feature request (on referencing) if you are missing an API for the kind of customization you need.

| Package | Count |
|---------|-------|
| `invenio-administration` | 2 |
| `invenio-audit-logs` | 2 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-drafts-resources` | 2 |
| `invenio-jobs` | 2 |
| `invenio-notifications` | 2 |
| `invenio-pages` | 2 |

#### Warning 4 - 16 occurrences

RemovedInMarshmallow4Warning: The `context` parameter is deprecated and will be removed in marshmallow 4.0. Use `contextvars.ContextVar` to pass context instead.

| Package | Count |
|---------|-------|
| `invenio-jobs` | 4 |
| `invenio-audit-logs` | 3 |
| `invenio-drafts-resources` | 3 |
| `invenio-banners` | 2 |
| `invenio-checks` | 2 |
| `invenio-pages` | 2 |

#### Warning 5 - 10 occurrences

RemovedInMarshmallow4Warning: The 'default' argument to fields is deprecated. Use 'dump_default' instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 2 |
| `invenio-jobs` | 2 |
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 6 - 9 occurrences

DeprecationWarning: 'crypt' is deprecated and slated for removal in Python 3.13

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 7 - 8 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('fs.opener')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 8 - 8 occurrences

DeprecationWarning: Deprecated call to `pkg_resources.declare_namespace('sphinxcontrib')`.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 9 - 8 occurrences

DeprecationWarning: The '__version_info__' attribute is deprecated and will be removed in in a future version. Use feature detection or 'packaging.Version(importlib.metadata.version("marshmallow")).release' instead.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 10 - 8 occurrences

DeprecationWarning: jsonschema.exceptions.RefResolutionError is deprecated as of version 4.18.0. If you wish to catch potential reference resolution errors, directly catch referencing.exceptions.Unresolvable.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 11 - 8 occurrences

UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-notifications` | 1 |
| `invenio-pages` | 1 |

#### Warning 12 - 7 occurrences

DeprecationWarning: Using the initialization functions in flask_caching.backend is deprecated.  Use the a full path to backend classes directly.

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 13 - 7 occurrences

FutureWarning: CSRF validation will be enabled by default in the version 1.3.x

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-github` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 14 - 6 occurrences

DeprecationWarning: Link is deprecated and will be removed in v14.0. Use `ExternalLink` for third-party links and `EndpointLink` for InvenioRDM links.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |
| `invenio-banners` | 1 |
| `invenio-checks` | 1 |
| `invenio-drafts-resources` | 1 |
| `invenio-jobs` | 1 |
| `invenio-pages` | 1 |

#### Warning 15 - 6 occurrences

SAWarning: nested transaction already deassociated from connection

| Package | Count |
|---------|-------|
| `invenio-pages` | 6 |

#### Warning 16 - 3 occurrences

DeprecationWarning: datetime.datetime.utcfromtimestamp() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.fromtimestamp(timestamp, datetime.UTC).

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-github` | 1 |
| `invenio-pages` | 1 |

#### Warning 17 - 2 occurrences

ChangedInMarshmallow4Warning: `Field` should not be instantiated. Use `fields.Raw` or  another field subclass instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |
| `invenio-jobs` | 1 |

#### Warning 18 - 2 occurrences

DeprecationWarning: get_user method is deprecated, user get_user_by_email/get_user_by_id

| Package | Count |
|---------|-------|
| `invenio-banners` | 1 |
| `invenio-pages` | 1 |

#### Warning 19 - 1 occurrence

DeprecationWarning: Implicit imports (e.g., 'import idutils; idutils.function;') might be removed in the next major version. Please use explicit imports (e.g., 'from idutils import function;') instead.

| Package | Count |
|---------|-------|
| `invenio-checks` | 1 |

#### Warning 20 - 1 occurrence

DeprecationWarning: No path_separator found in configuration; falling back to legacy splitting on spaces/commas for version_locations.  Consider adding path_separator=os to Alembic config.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 21 - 1 occurrence

DeprecationWarning: Remember me support has been removed.

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 22 - 1 occurrence

DeprecationWarning: The 'record_to_index' function is no longer expected to return a tuple (index, doc_type), instead it should only return the index. Support for the tuple will be removed in a future version of 'invenio-indexer'.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 23 - 1 occurrence

DeprecationWarning: The 'warn' method is deprecated, use 'warning' instead

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 24 - 1 occurrence

LegacyAPIWarning: The Query.get() method is considered legacy as of the 1.x series of SQLAlchemy and becomes a legacy construct in 2.0. The method is now available as Session.get() (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 25 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestCustomView' because it has a __init__ constructor (from: tests/test_base.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 26 - 1 occurrence

PytestCollectionWarning: cannot collect test class 'TestSchema' because it has a __init__ constructor (from: tests/test_marshmallow_utils.py)

| Package | Count |
|---------|-------|
| `invenio-administration` | 1 |

#### Warning 27 - 1 occurrence

RemovedInMarshmallow4Warning: The 'missing' argument to fields is deprecated. Use 'load_default' instead.

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 28 - 1 occurrence

SADeprecationWarning: The from_engine() method on Inspector is deprecated and will be removed in a future release.  Please use the sqlalchemy.inspect() function on an Engine or Connection in order to acquire an Inspector. (deprecated since: 1.4)

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |

#### Warning 29 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('004cddd5-e977-40b2-8bc3-7498bc66e2d6'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 30 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('0253ffc9-d9d9-43ea-918e-b83451d628bc'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 31 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('32d233b2-d4df-45d4-a462-6bbcbd9c7677'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 32 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('3d5a5db7-3864-4591-a1a0-64786f95b514'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 33 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('67655926-c67a-4b60-8d37-2561545fecc2'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 34 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('a183e5bb-f1cc-4477-b546-7466c573a9c5'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 35 - 1 occurrence

SAWarning: Identity map already had an identity for (<class 'invenio_jobs.models.Run'>, (UUID('c4c86cdd-5cc2-4c62-a9d9-4870cca8758a'),), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?

| Package | Count |
|---------|-------|
| `invenio-jobs` | 1 |

#### Warning 36 - 1 occurrence

SAWarning: Object of type <ObjectVersion> not in session, add operation along 'Bucket.objects' will not proceed (This warning originated from the Session 'autoflush' process, which was invoked automatically in response to a user-initiated operation. Consider using ``no_autoflush`` context manager if this warning happened while initializing objects.)

| Package | Count |
|---------|-------|
| `invenio-drafts-resources` | 1 |

#### Warning 37 - 1 occurrence

UserWarning: autoincrement and existing_autoincrement only make sense for MySQL

| Package | Count |
|---------|-------|
| `invenio-audit-logs` | 1 |




---