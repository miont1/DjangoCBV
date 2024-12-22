import graphene
import recipes.schema


class Query(recipes.schema.Query, graphene.ObjectType):
    pass


class Mutation(recipes.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
