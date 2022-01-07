import pytest

from d2e_share_splitter.shareconf.factories import ProjectFactory
from d2e_share_splitter.shareconf.models import Project
from d2e_share_splitter.sharecontributions.factories import (
    ContributionTime10hFactory,
)  # NOQA
from d2e_share_splitter.sharecontributions.models import Contribution
from d2e_share_splitter.sharecontributions.utils import (
    compute_contrib_pie_slices,
)  # NOQA
from d2e_share_splitter.users.tests.factories import UserFactoryNoSlices


@pytest.mark.django_db
class TestComputeSlices:
    def test_utility_function(self):
        year_salary = 55000
        hourly_rate = year_salary / 2000
        user = UserFactoryNoSlices(yearSalary=year_salary)
        project: Project = ProjectFactory()
        contribution: Contribution = ContributionTime10hFactory(
            project=project, user=user
        )
        assert contribution.slices == 0

        compute_contrib_pie_slices(contribution)

        contribution.refresh_from_db()
        expected_slices = hourly_rate * 10 * project.non_cash_multiplier
        assert contribution.slices == expected_slices

        user.refresh_from_db()
        assert user.slices == expected_slices
