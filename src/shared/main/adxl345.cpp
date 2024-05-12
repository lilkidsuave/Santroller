#include "io.h"
#include "adxl.h"
#include "fxpt_math.h"
#include "config.h"
int16_t filtered[3] = {0};
#ifdef INPUT_ADXL
void init_adxl() {
    twi_writeSingleToPointer(ADXL_TWI_PORT, ADXL345_ADDRESS, ADXL345_POWER_CTL, 0x08);
    twi_writeSingleToPointer(ADXL_TWI_PORT, ADXL345_ADDRESS, ADXL345_DATA_FORMAT, 0x0B);
}
void tick_adxl() {
    int16_t filtered[3] = {0};  // Initialize filtered data array
    int16_t raw[3];
    twi_readFromPointer(ADXL_TWI_PORT, ADXL345_ADDRESS, ADXL345_DATAX0, 6, (uint8_t*)raw);
    for (int i = 0; i < 3; i++) {
        if (i == 1) {  // Check if Y-axis
            raw[i] *= -1;  // Invert Y-axis value
        }
        // Apply filtering and store in filtered array
        filtered[i] = (raw[i] * 64) * LOW_PASS_ALPHA + (filtered[i] * (1.0 - LOW_PASS_ALPHA));
    }
}
#endif
