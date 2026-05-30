# Storage Specification

## Purpose

Centralized storage system for images, generated 3D models, previews, and user files.

## Storage Provider

- Amazon S3 compatible storage
- Private buckets
- Secure file access

## Stored Objects

### Source Images

- Uploaded by users
- JPG
- PNG
- WEBP

### Generated Models

- GLB
- GLTF

### Preview Files

- PNG
- JPG

## Directory Structure

uploads/
├── images/
├── previews/
└── models/

## Upload Workflow

1. User uploads image
2. Backend validates image
3. Image stored in S3
4. Storage URL saved in database

## Download Workflow

1. User requests model
2. Backend verifies access
3. Temporary download URL generated
4. File downloaded

## Security

- Private buckets
- Signed URLs
- Access validation
- User ownership verification

## File Limits

### Images

- Maximum size: 20 MB

### Models

- Maximum size: 500 MB

## Backup Strategy

- Daily backup
- Versioning enabled
- Recovery support

## Monitoring

- Storage usage
- Upload failures
- Download failures

## Error Handling

- Missing file
- Corrupted file
- Upload failure
- Download failure

## Future Improvements

- CDN integration
- Multi-region storage
- Automatic optimization