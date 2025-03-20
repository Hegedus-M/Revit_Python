def schema_creator(element_in, data_in):
    # create a schemaBuilder
    schemaGuid = Guid.NewGuid()
    schemaBuilder = ExtensibleStorage.SchemaBuilder(schemaGuid)

    # set read/write access
    schemaBuilder.SetReadAccessLevel(ExtensibleStorage.AccessLevel.Public)
    schemaBuilder.SetWriteAccessLevel(ExtensibleStorage.AccessLevel.Public)

    # set the schema name
    schemaBuilder.SetSchemaName("Example_Schema")

    # add fields to the schema
    """Ensure data type specified in the AddSimpleField below matches the data type data_in"""
    example_field = schemaBuilder.AddSimpleField("Example_Field", String)

    # set field documentation
    example_field.SetDocumentation("Description of what Example_Field is")

    # create the schema using the above schemaBuilder
    schema = schemaBuilder.Finish()
    entity = ExtensibleStorage.Entity(schema)

    # get the field from the schema
    example_field = schema.GetField("Example_Field")

    # set the value of the field to the information from data_in
    entity.Set[String](example_field, data_in)
    element_in.SetEntity(entity)

    return schema.GUID


def schema_retriever(element_in):
    # get the schemas from the data_in
    schemas = element_in.GetEntitySchemaGuids()

    # get the schema names from the schemas
    schemaNames = [ExtensibleStorage.Schema.Lookup(schema).SchemaName for schema in schemas]

    # check if schema exists and retrieve parameter values
    if "Example_Schema" in schemaNames:
        index = schemaNames.index("Example_Schema")
        schemaGuid = schemas[index]
        schema = ExtensibleStorage.Schema.Lookup(schemaGuid)

        # get existing schema parameter values
        example_field = schema.GetField("Example_Field")
        data_out = element_in.GetEntity(schema).Get[String](example_field)

        return data_out

    else:
        raise NameError("Unable to find matching schema")