import time

def get_variable_dict(variables):

  variables_dict = dict()

  for i in range(len(variables.index)):

    for val in variables.index:

      variables_dict[f'{i}_to_{val}'] = 0

  return variables_dict


def count_mapping_groupwise_samples(variables, df, y_pred):

  # print('\nCalculating sample counts to every mapping group...')

  for i in range(len(y_pred)):

    int_label = y_pred[i]
    string_label = df.iloc[i]['class']

    variables[f'{int_label}_to_{string_label}'] += 1

  return variables


def get_mapping_result(variables, actual_labels):

  mapping_percentage = dict()

  for label in actual_labels.index:
    for key in variables:
      if key.find(label) != -1:
        mapping_percentage[key] = (variables[key]/actual_labels[label])*100
  
  return mapping_percentage


def is_conflict(calculated_class_labels):

  flipped = dict()

  for key, value in calculated_class_labels.items():

    flipped.setdefault(value, set()).add(key)

  # print(flipped)

  duplicates = [key for key, values in flipped.items() if len(values) > 1]

  # print(duplicates)

  return duplicates



def get_resolved_class_labels(mapping_percentage, calculated_class_labels, conflict_labels):

  # print('--------')
  # print('calculated class labels: ', calculated_class_labels)

  # print('---------')
  # print(conflict_labels)

  # print('---------')

  for label in conflict_labels:

    temp_dict = { key: value for key, value in mapping_percentage.items() if key.find(str(label)) != -1 }

    # print(possible_labels)

    # print('temp dict: ', temp_dict)

    count = 1
    for key, value in sorted(temp_dict.items(), key=lambda x: x[1], reverse=True):

      available_labels = [i for i in range(len(calculated_class_labels)) if i not in calculated_class_labels.values()]

      current_key = key.split('_to_')[-1]
      
      if count == 1:
        calculated_class_labels[current_key] = label

        # print('calculated class labels ->', calculated_class_labels)
        
      else:
        calculated_class_labels[current_key] = min(available_labels)
      
      # print('Available labels: ', available_labels)
    
      count += 1

  print('After resolving: ', calculated_class_labels)

  return calculated_class_labels


def get_calculated_class_labels(mapping_percentage, actual_labels):

  print(mapping_percentage)

  calculated_class_labels = dict()

  for label in actual_labels.index:

    # print(label, end="\n\n")

    class_percentage = { key: value for key, value in mapping_percentage.items() if key.find(label) != -1 }

    # print(class_percentage, end="\n\n")

    max_key = max(class_percentage, key=class_percentage.get)

    # print(max_key, end="\n\n")

    calculated_class_labels[label] = int(max_key.split('_to_')[0])

    # print(calculated_class_labels, end="\n\n\n")


  conflict_labels = is_conflict(calculated_class_labels)

  if conflict_labels:

    print('CONFLICT')

    calculated_class_labels = get_resolved_class_labels(mapping_percentage, calculated_class_labels, conflict_labels)

  else:

    print('NO CONFLICT')

    print(calculated_class_labels)


  return calculated_class_labels


def get_mapped_class_labels(df, class_attribute, calculated_class_labels):

  y_true = df[class_attribute].apply(lambda x: calculated_class_labels[x])

  return y_true


def get_mapped_actual_class_labels(df, class_attribute, actual_labels, y_pred):

  variables = get_variable_dict(actual_labels)

  variables = count_mapping_groupwise_samples(variables, df, y_pred)

  mapping_percentage = get_mapping_result(variables, actual_labels)
  
  calculated_class_labels = get_calculated_class_labels(mapping_percentage, actual_labels)

  mapped_class_labels = get_mapped_class_labels(df, class_attribute, calculated_class_labels)

  # print(y_pred)

  # print(mapped_class_labels)

  # print(df['class'])

  return mapped_class_labels