from setuptools import setup


setup(
    name='cldfbench_sagart_et_al2019',
    py_modules=['cldfbench_sagart_et_al2019'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'sagart_et_al2019=cldfbench_sagart_et_al2019:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
