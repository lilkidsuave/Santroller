#include <stdbool.h>
#include <stdint.h>
#include "descriptors.h"

extern uint8_t deviceType;
extern bool guitar;
extern bool drum;

void init(void);
void tick(void);