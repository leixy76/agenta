"""initial migration for first time and returning users

Revision ID: b80c708c21bb
Revises: 
Create Date: 2024-07-11 13:20:31.705894

"""
from typing import Sequence, Union

from alembic import op
from alembic import context

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from agenta_backend.migrations.postgres.utils import is_initial_setup


# revision identifiers, used by Alembic.
revision: str = "b80c708c21bb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def first_time_user_from_agenta_v019_upwards_upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ids_mapping",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("table_name", sa.String(), nullable=False),
        sa.Column("objectid", sa.String(), nullable=False),
        sa.Column("uuid", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "templates",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("type", sa.Enum("IMAGE", "ZIP", name="templatetype"), nullable=False),
        sa.Column("template_uri", sa.String(), nullable=True),
        sa.Column("tag_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("repo_name", sa.String(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("digest", sa.String(), nullable=True),
        sa.Column("last_pushed", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("uid", sa.String(), nullable=True),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("id"),
    )
    op.create_index(op.f("ix_users_uid"), "users", ["uid"], unique=True)
    op.create_table(
        "app_db",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_name", sa.String(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "docker_images",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("template_uri", sa.String(), nullable=True),
        sa.Column("docker_id", sa.String(), nullable=True),
        sa.Column("tags", sa.String(), nullable=True),
        sa.Column("deletable", sa.Boolean(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_index(
        op.f("ix_docker_images_docker_id"), "docker_images", ["docker_id"], unique=False
    )
    op.create_table(
        "deployments",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("container_name", sa.String(), nullable=True),
        sa.Column("container_id", sa.String(), nullable=True),
        sa.Column("uri", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "evaluators_configs",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("evaluator_key", sa.String(), nullable=True),
        sa.Column(
            "settings_values", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "testsets",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("csvdata", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "bases",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("base_name", sa.String(), nullable=True),
        sa.Column("image_id", sa.UUID(), nullable=True),
        sa.Column("deployment_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["deployment_id"], ["deployments.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["image_id"], ["docker_images.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "human_evaluations",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("status", sa.String(), nullable=True),
        sa.Column("evaluation_type", sa.String(), nullable=True),
        sa.Column("testset_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["testset_id"],
            ["testsets.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "app_variants",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("variant_name", sa.String(), nullable=True),
        sa.Column("revision", sa.Integer(), nullable=True),
        sa.Column("image_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("modified_by_id", sa.UUID(), nullable=True),
        sa.Column("base_name", sa.String(), nullable=True),
        sa.Column("base_id", sa.UUID(), nullable=True),
        sa.Column("config_name", sa.String(), nullable=False),
        sa.Column(
            "config_parameters", postgresql.JSONB(astext_type=sa.Text()), nullable=False
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["base_id"],
            ["bases.id"],
        ),
        sa.ForeignKeyConstraint(
            ["image_id"], ["docker_images.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "human_evaluations_scenarios",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("evaluation_id", sa.UUID(), nullable=True),
        sa.Column("inputs", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("outputs", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("vote", sa.String(), nullable=True),
        sa.Column("score", sa.String(), nullable=True),
        sa.Column("correct_answer", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("is_pinned", sa.Boolean(), nullable=True),
        sa.Column("note", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["evaluation_id"], ["human_evaluations.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "app_variant_revisions",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("variant_id", sa.UUID(), nullable=True),
        sa.Column("revision", sa.Integer(), nullable=True),
        sa.Column("modified_by_id", sa.UUID(), nullable=True),
        sa.Column("base_id", sa.UUID(), nullable=True),
        sa.Column("config_name", sa.String(), nullable=False),
        sa.Column(
            "config_parameters", postgresql.JSONB(astext_type=sa.Text()), nullable=False
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["base_id"],
            ["bases.id"],
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["variant_id"], ["app_variants.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "environments",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("revision", sa.Integer(), nullable=True),
        sa.Column("deployed_app_variant_id", sa.UUID(), nullable=True),
        sa.Column("deployed_app_variant_revision_id", sa.UUID(), nullable=True),
        sa.Column("deployment_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["deployed_app_variant_id"], ["app_variants.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["deployed_app_variant_revision_id"],
            ["app_variant_revisions.id"],
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["deployment_id"], ["deployments.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "evaluations",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("app_id", sa.UUID(), nullable=True),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("status", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("testset_id", sa.UUID(), nullable=True),
        sa.Column("variant_id", sa.UUID(), nullable=True),
        sa.Column("variant_revision_id", sa.UUID(), nullable=True),
        sa.Column(
            "average_cost", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("total_cost", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "average_latency", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["app_id"], ["app_db.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["testset_id"], ["testsets.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["variant_id"], ["app_variants.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["variant_revision_id"], ["app_variant_revisions.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "human_evaluation_variants",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("human_evaluation_id", sa.UUID(), nullable=True),
        sa.Column("variant_id", sa.UUID(), nullable=True),
        sa.Column("variant_revision_id", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["human_evaluation_id"], ["human_evaluations.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["variant_id"], ["app_variants.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["variant_revision_id"], ["app_variant_revisions.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "environments_revisions",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("environment_id", sa.UUID(), nullable=True),
        sa.Column("revision", sa.Integer(), nullable=True),
        sa.Column("modified_by_id", sa.UUID(), nullable=True),
        sa.Column("deployed_app_variant_revision_id", sa.UUID(), nullable=True),
        sa.Column("deployment_id", sa.UUID(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["deployed_app_variant_revision_id"],
            ["app_variant_revisions.id"],
            ondelete="SET NULL",
        ),
        sa.ForeignKeyConstraint(
            ["deployment_id"], ["deployments.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["environment_id"], ["environments.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["modified_by_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "evaluation_aggregated_results",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("evaluation_id", sa.UUID(), nullable=True),
        sa.Column("evaluator_config_id", sa.UUID(), nullable=True),
        sa.Column("result", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(
            ["evaluation_id"], ["evaluations.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["evaluator_config_id"], ["evaluators_configs.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "evaluation_evaluator_configs",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("evaluation_id", sa.UUID(), nullable=False),
        sa.Column("evaluator_config_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["evaluation_id"], ["evaluations.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["evaluator_config_id"], ["evaluators_configs.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id", "evaluation_id", "evaluator_config_id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "evaluation_scenarios",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("evaluation_id", sa.UUID(), nullable=True),
        sa.Column("variant_id", sa.UUID(), nullable=True),
        sa.Column("inputs", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("outputs", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "correct_answers", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
        sa.Column("is_pinned", sa.Boolean(), nullable=True),
        sa.Column("note", sa.String(), nullable=True),
        sa.Column("latency", sa.Integer(), nullable=True),
        sa.Column("cost", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(
            ["evaluation_id"], ["evaluations.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["variant_id"], ["app_variants.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "evaluation_scenario_results",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("evaluation_scenario_id", sa.UUID(), nullable=True),
        sa.Column("evaluator_config_id", sa.UUID(), nullable=True),
        sa.Column("result", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.ForeignKeyConstraint(
            ["evaluation_scenario_id"], ["evaluation_scenarios.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["evaluator_config_id"], ["evaluators_configs.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def returning_user_from_agenta_v018_downwards_upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "app_db", ["id"])
    op.create_unique_constraint(None, "app_variant_revisions", ["id"])
    op.create_unique_constraint(None, "app_variants", ["id"])
    op.create_unique_constraint(None, "bases", ["id"])
    op.create_unique_constraint(None, "deployments", ["id"])
    op.create_unique_constraint(None, "docker_images", ["id"])
    op.create_unique_constraint(None, "environments", ["id"])
    op.create_unique_constraint(None, "environments_revisions", ["id"])
    op.create_unique_constraint(None, "evaluation_aggregated_results", ["id"])
    op.create_unique_constraint(None, "evaluation_scenario_results", ["id"])
    op.create_unique_constraint(None, "evaluation_scenarios", ["id"])
    op.create_unique_constraint(None, "evaluations", ["id"])
    op.create_unique_constraint(None, "evaluators_configs", ["id"])
    op.create_unique_constraint(None, "human_evaluation_variants", ["id"])
    op.create_unique_constraint(None, "human_evaluations", ["id"])
    op.create_unique_constraint(None, "human_evaluations_scenarios", ["id"])
    op.create_unique_constraint(None, "ids_mapping", ["id"])
    op.create_unique_constraint(None, "templates", ["id"])
    op.create_unique_constraint(None, "testsets", ["id"])
    op.create_unique_constraint(None, "users", ["id"])
    # ### end Alembic commands ###


def first_time_user_from_agenta_v019_upwards_downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("evaluation_scenario_results")
    op.drop_table("evaluation_scenarios")
    op.drop_table("evaluation_evaluator_configs")
    op.drop_table("evaluation_aggregated_results")
    op.drop_table("environments_revisions")
    op.drop_table("human_evaluation_variants")
    op.drop_table("evaluations")
    op.drop_table("environments")
    op.drop_table("app_variant_revisions")
    op.drop_table("human_evaluations_scenarios")
    op.drop_table("app_variants")
    op.drop_table("human_evaluations")
    op.drop_table("bases")
    op.drop_table("testsets")
    op.drop_table("evaluators_configs")
    op.drop_table("deployments")
    op.drop_index(op.f("ix_docker_images_docker_id"), table_name="docker_images")
    op.drop_table("docker_images")
    op.drop_table("app_db")
    op.drop_index(op.f("ix_users_uid"), table_name="users")
    op.drop_table("users")
    op.drop_table("templates")
    op.drop_table("ids_mapping")
    # ### end Alembic commands ###


def returning_user_from_agenta_v018_downwards_downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.drop_constraint(None, "testsets", type_="unique")
    op.drop_constraint(None, "templates", type_="unique")
    op.drop_constraint(None, "ids_mapping", type_="unique")
    op.drop_constraint(None, "human_evaluations_scenarios", type_="unique")
    op.drop_constraint(None, "human_evaluations", type_="unique")
    op.drop_constraint(None, "human_evaluation_variants", type_="unique")
    op.drop_constraint(None, "evaluators_configs", type_="unique")
    op.drop_constraint(None, "evaluations", type_="unique")
    op.drop_constraint(None, "evaluation_scenarios", type_="unique")
    op.drop_constraint(None, "evaluation_scenario_results", type_="unique")
    op.drop_constraint(None, "evaluation_aggregated_results", type_="unique")
    op.drop_constraint(None, "environments_revisions", type_="unique")
    op.drop_constraint(None, "environments", type_="unique")
    op.drop_constraint(None, "docker_images", type_="unique")
    op.drop_constraint(None, "deployments", type_="unique")
    op.drop_constraint(None, "bases", type_="unique")
    op.drop_constraint(None, "app_variants", type_="unique")
    op.drop_constraint(None, "app_variant_revisions", type_="unique")
    op.drop_constraint(None, "app_db", type_="unique")
    # ### end Alembic commands ###


def upgrade() -> None:
    engine = sa.create_engine(context.config.get_main_option("sqlalchemy.url"))
    if is_initial_setup(engine=engine):
        first_time_user_from_agenta_v019_upwards_upgrade()
    else:
        returning_user_from_agenta_v018_downwards_upgrade()


def downgrade() -> None:
    engine = sa.create_engine(context.config.get_main_option("sqlalchemy.url"))
    if is_initial_setup(engine=engine):
        first_time_user_from_agenta_v019_upwards_downgrade()
    else:
        returning_user_from_agenta_v018_downwards_downgrade()
