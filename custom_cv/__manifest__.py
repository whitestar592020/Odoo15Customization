{
    "name": "Custom CV",
    "website": "https://www.facebook.com/odooerpdevelopment",
    "category": "Productivity",
    "summary": "Custom module to customize the CV Form app!",
    "author": "White Star Myanmar education center",
    "application": False,
    "depends": ["curriculum_vitae"],

    "data": [
        "views/inherit_cv_view_form.xml",
        "views/inherit_cv_view_kanban.xml",
        "views/inherit_cv_view_search.xml",
        "views/inherit_cv_view_tree.xml",
        "views/inherit_cv_view_reporting.xml",
        "views/standard_cv_view_activity.xml",
        "report/inherit_cv_report_pdf.xml",

        "security/ir.model.access.csv",
        "views/custom_cv_views.xml",
        "views/education_views.xml",
        "views/experience_views.xml",
        "views/project_views.xml",
        "views/language_views.xml",
        "views/custom_cv_view_tree.xml",
        "views/custom_cv_view_search.xml",
        "views/custom_cv_view_kanban.xml",
        "views/custom_cv_view_reporting.xml",

        "report/custom_cv_report_pdf.xml",
        "report/custom_cv_report_template.xml",
        "report/custom_cv_report_preview.xml",
        "views/custom_cv_view_form.xml",
    ],

    'assets': {
        'web.assets_qweb': [
            'custom_cv/static/src/xml/language.xml',
        ],
        'web.assets_backend': [
            'custom_cv/static/src/js/language.js',
            'custom_cv/static/src/css/language.css',
        ],
    },

    "demo": [
        "data/custom_cv_demo.xml",
    ],
}
