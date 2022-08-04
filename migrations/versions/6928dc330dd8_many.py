"""many

Revision ID: 6928dc330dd8
Revises: 
Create Date: 2022-08-01 12:47:21.697814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6928dc330dd8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('slug'),
    sa.UniqueConstraint('title')
    )
    op.create_table('tags',
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('slug'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('activation_code', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('slug', sa.String(length=100), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('category_id', sa.String(length=50), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.slug'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_posts_slug'), 'posts', ['slug'], unique=True)
    op.create_table('post_tag',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.slug'], ),
    sa.PrimaryKeyConstraint('post_id', 'tag_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tag')
    op.drop_index(op.f('ix_posts_slug'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('tags')
    op.drop_table('categories')
    # ### end Alembic commands ###