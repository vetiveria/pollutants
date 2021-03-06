"""Module main"""
import os
import sys
import logging
import collections

import argparse


def main():
    """
    Entry point
    :return:
    """

    #  Prepare directories
    directories.cleanup(directories_=[configurations.warehouse])
    directories.create(directories_=[configurations.warehouse])

    # Schema attributes
    usecols, dtype = read_schema.exc(schema_url=parameters.schema_url)

    # Data specifications
    DataSpecifications = collections.namedtuple(typename='DataSpecifications',
                                                field_names=['data_url', 'usecols', 'dtype', 'rename', 'dictionary_of_names'])
    specifications = DataSpecifications._make((parameters.data_url, usecols, dtype,
                                               parameters.rename, parameters.dictionary_of_names))

    # Hence, read the data
    read_data = pollutants.src.readdata.ReadData(specifications=specifications)
    data = read_data.exc()
    logger.info('\n %s', data.info())

    # Retain valid data instances only
    data = instances.exc(data=data.copy())
    logger.info('\n %s', data.info())
    logger.info('\n %s', data.head())

    # Save
    data.to_csv(path_or_buf=os.path.join(configurations.warehouse, 'pollutants.csv'), header=True, index=False,
                encoding='UTF-8')


if __name__ == '__main__':
    # Preliminaries
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'toxicants'))

    # Logging
    logging.basicConfig(level=logging.INFO, format='%(message)s\n%(asctime)s.%(msecs)03d', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # Libraries
    import config
    import pollutants.io.arguments
    import pollutants.io.directories
    import pollutants.src.readschema
    import pollutants.src.readdata
    import pollutants.algorithms.instances

    # Arguments
    arguments = pollutants.io.arguments.Arguments()
    parser = argparse.ArgumentParser()
    parser.add_argument('elements', type=arguments.url, help='The URL of a YAML of parameters; refer to the '
                                                             'README notes.  The argument parser returns a blob of elements')
    args = parser.parse_args()
    parameters = arguments.parameters(elements=args.elements)

    # Hence
    configurations = config.Config()
    directories = pollutants.io.directories.Directories()
    read_schema = pollutants.src.readschema.ReadSchema()
    instances = pollutants.algorithms.instances.Instances()

    main()
