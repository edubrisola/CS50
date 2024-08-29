#include <stdint.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // Open memory card file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    // Buffer for reading
    uint8_t buffer[512];

    // Counter for file names
    int count = 0;

    // File pointer for current JPEG
    FILE *img = NULL;

    // Read until end of file
    while (fread(buffer, sizeof(uint8_t), 512, file) == 512)
    {
        // Check if the current block is the start of a new JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            // Close previous JPEG file if it exists
            if (img != NULL)
            {
                fclose(img);
            }

            // Create new JPEG file
            char filename[8];
            sprintf(filename, "%03i.jpg", count++);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                printf("Could not create file.\n");
                return 1;
            }
        }

        // Write buffer to JPEG file
        if (img != NULL)
        {
            fwrite(buffer, sizeof(uint8_t), 512, img);
        }
    }

    // Close any remaining files
    if (img != NULL)
    {
        fclose(img);
    }

    // Close memory card file
    fclose(file);

    return 0;
}
