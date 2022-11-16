function getColorCode(age: number | null) {
    var color: string | null = null;
    var current_age: number | null = null;

    if (age != null) {
        current_age = age;
    }

    if (current_age != null) {
        if (current_age < 12 ? true : false) {
            color = 'red';
        }
    }
    if (current_age != null) {
        if (current_age < 16 ? true : false) {
            color = 'yellow';
        }
    }
    if (current_age != null) {
        if (current_age < 18 ? true : false) {
            color = 'green';
        }
    }

    switch (color) {
        case 'green':
            return 0;
            break;
        case 'yellow':
            return 1;
            break;
        case 'red':
            return 2;
            break;

    }
}